# toWebHtmlMacro.py
# -*- coding: utf-8 -*-
# LibreOfficeのディスパッチコマンドでウェブブラウザに出力するマクロ。
from com.sun.star.beans import PropertyValue 
def toWebHtml():
    desktop = XSCRIPTCONTEXT.getDesktop()  # デスクトップを取得。
    prop = PropertyValue(Name="Hidden",Value=True)  # バックグラウンドで開く設定。
    doc = desktop.loadComponentFromURL("private:factory/swriter", "_blank", 0, (prop,))  # バックグラウンドでWriterのドキュメントを開く。
    doc.getText().setString("toWebHTML拡張機能から出力")  # Writerドキュメントに文字列を出力。
    frame = doc.getCurrentController().getFrame() #Writerドキュメントのフレームの取得。
    ctx = XSCRIPTCONTEXT.getComponentContext() #コンポーネントコンテクストの取得。
    smgr = ctx.getServiceManager()  # サービスマネジャーの取得。
    dispatcher = smgr.createInstanceWithContext("com.sun.star.frame.DispatchHelper",ctx) #com.sun.star.frame.DispatchHelperのUNOインスタンスを取得。
    dispatcher.executeDispatch(frame, ".uno:WebHtml", "", 0, tuple())  # .uno;WebHtmlでデフォルトウェブブラウザに出力する。
    doc.close(True)  # バックグラウンドで開いたドキュメントを閉じる。
g_exportedScripts = toWebHtml,  # マクロセレクターに表示させる関数を制限。

