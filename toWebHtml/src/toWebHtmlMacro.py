# toWebHtmlMacro.py
# -*- coding: utf-8 -*-
from com.sun.star.beans import PropertyValue 
def toWebHtml():
    desktop = XSCRIPTCONTEXT.getDesktop()
    prop = PropertyValue(Name="Hidden",Value=True)
    doc = desktop.loadComponentFromURL("private:factory/swriter", "_blank", 0, (prop,))  # バックグラウンドでWriterのドキュメントを開く。
    doc.getText().setString("ウェブブラウザに出力する文字列")  # Writerドキュメントに出力。
    frame = doc.getCurrentController().getFrame() #フレームの取得。
    ctx = XSCRIPTCONTEXT.getComponentContext() #コンポーネントコンテクストの取得。
    smgr = ctx.getServiceManager()  # サービスマネジャーの取得。
    dispatcher = smgr.createInstanceWithContext("com.sun.star.frame.DispatchHelper",ctx) #com.sun.star.frame.DispatchHelperのUNOインスタンスを取得。
    dispatcher.executeDispatch(frame, ".uno:WebHtml", "", 0, tuple())
    doc.close(True)
g_exportedScripts = toWebHtml,

