from com.ibm.json.java import JSONArray, JSONObject
from psdi.mbo import  MboSet, MboConstants
from psdi.server import MXServer 
from java.nio.charset import StandardCharsets
from java.io import BufferedReader, InputStreamReader, OutputStream
from java.net import URL, HttpURLConnection , URLEncoder
from sys import *
from java.lang import *
from java.util import *
from java.io import InputStreamReader
from java.io import BufferedReader
from org.json.simple.parser import JSONParser

mxServer = MXServer.getMXServer()
userInfo = mxServer.getUserInfo("MAXADMIN")

PropSet = MXServer.getMXServer().getMboSet("maxpropvalue", userInfo)
PropSet.setWhere("PROPNAME = 'chatgpt.answers.url'")
PropSet.reset()
if PropSet.isEmpty() == False:
	propMbo = PropSet.getMbo(0)
	tCxtURL = str(propMbo.getString("PROPVALUE"))
	
PropSet = MXServer.getMXServer().getMboSet("maxpropvalue", userInfo)
PropSet.setWhere("PROPNAME = 'chatgpt.apikey'")
PropSet.reset()
if PropSet.isEmpty() == False:
  propMbo = PropSet.getMbo(0)
  apiKey = str(propMbo.getString("PROPVALUE"))

question=mbo.getString("QUESTION")
jsonStr = ""
obj = JSONObject()
obj.put("model","text-davinci-003") 
obj.put("max_tokens", 50)   
obj.put("temperature", 0.5)
obj.put("prompt",question)
jsonStr = obj.serialize(True)

url = URL(str(tCxtURL))
con = url.openConnection()
con.setRequestProperty('Authorization',"Bearer " + apiKey)
con.setRequestMethod('POST')
con.setRequestProperty('Content-Type', 'application/json')
con.setDoOutput(True)
os = con.getOutputStream()

os.write(str(jsonStr))
resp = con.getResponseCode()
os.flush()
os.close()
  
if resp ==200:
	reader =  BufferedReader( InputStreamReader(con.getInputStream()));
	line =reader.readLine()
	parse=JSONParser()
	jobj=JSONObject()	
	jobj=parse.parse(line)
	choices_array=jobj.get("choices")
	for choice in choices_array:
	    text = choice.get("text")
	#raise TypeError(text)
	mbo.setValue("RESPONSE",text,11l)
	con.disconnect()

else:
  reader =  BufferedReader( InputStreamReader(con.getErrorStream()))
  line =reader.readLine() 
  parse=JSONParser()
  jobj=JSONObject()
  jobj=parse.parse(line)
  message=jobj.get("error").get("message")
  con.disconnect()     
  raise TypeError("Error Connecting with ChatGPT :"+ message)