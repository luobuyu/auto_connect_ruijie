choice = msgbox("是否运行脚本", vbInformation+vbOKCancel, "提示")
if choice = vbOK then
	createobject("wscript.shell").run "python main.py",0
else
	msgbox "取消运行", vbInformation, "取消"
end if