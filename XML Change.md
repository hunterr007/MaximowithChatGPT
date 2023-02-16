<dialog id="C_CHATGPT" label="Ask from ChatGPT" relationship="C_CHATGPT">
	<section border="true" id="mxdwodialog_grid1">
		<sectionrow id="mxdwodialog_grid1_1">
		<sectioncol id="mxdwodialog_grid1_1_1">
			<textbox dataattribute="QUESTION" id="mxdwodialog_ques" Label="Question for ChatGPT"/>
			<multilinetextbox dataattribute="RESPONSE" id="mxdwodialog_resp1" label="Response from ChatGPT" rows="10"/>
		</sectioncol>
		</sectionrow>
	</section>
	<buttongroup id="mxdwodialog_2">
		<pushbutton id="mxdwodialog_2_1" label="Send Question" mxevent="C_OPENAPI"/>
		<pushbutton id="mxdwodialog_2_2" label="Close" mxevent="dialogcancel"/>
	</buttongroup>
</dialog>
