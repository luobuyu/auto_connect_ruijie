choice = msgbox("�Ƿ����нű�", vbInformation+vbOKCancel, "��ʾ")
if choice = vbOK then
	createobject("wscript.shell").run "python main.py",0
else
	msgbox "ȡ������", vbInformation, "ȡ��"
end if