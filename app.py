import flask

app = flask(__name__) #__name__是python內建的一個變數, 會儲存目前這個程式在哪個模組下進行執行
		      #如果這個程式是被當成主程式被執行的話__name__ = __main__
@app.route("/")	#函式的裝飾
def home():
	return "Hello Flask"

if __name__ == "__main__" : #如果把app.py當成主程式來運作
	app.run()	    #立刻執行app物件, 啟動服務器

