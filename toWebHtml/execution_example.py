#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
import traceback
def testCode(ctx, smgr):  # 引数はデコレーターで受け取る。ctx:サービスマネジャー、smgr: サービスマネジャー
    page = smgr.createInstanceWithContext("pq.ToWebHtml", ctx)
    page.setTitle("From toWebHtml Extension")
    page.openInBrowser("<span style='background-color: red;'>toWebHTML拡張機能から出力</span>")

# Service information to be instantiated instead of UNO component when in automation mode
# Class name, Implementation name, Service name
objinsp = "ToWebHtml", "pq.ToWebHtml", "com.blogspot.pq.ToWebHtml"
# Tuple of replacement service information
UNOCompos = objinsp,
# Function for test the source
func = testCode

# Function to call from macro
def macro():
    ctx = XSCRIPTCONTEXT.getComponentContext()
    smgr = ctx.getServiceManager()
    func(ctx, smgr)
g_exportedScripts = macro,
MODE = None
if __name__ == "__main__":
#     MODE = "Automation"
    from helpers.connectoffice import connectOffice
    with connectOffice(MODE, UNOCompos, func) as fn:
        fn()