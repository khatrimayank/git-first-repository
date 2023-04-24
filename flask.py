from flask import Flask , jsonify , request

app=Flask(__name__)



book_list=[
            {
             'id':0,

             'author':"china achebe",

             'language':'English',

             'title':"Things Fall Apart"
            },

           {
             'id':1,

             'author':"abcd",

             'language':"Danish",

             'title':"Fairy Tales"
            },

           {
             'id':2,

             'author':"efgh",

             'language':"German",

             'title':"cnksj"
            }
]

@app.route('/book',methods=['GET','POST'])

def book():
	if request.method=="GET":
		if len(book_list)>0:
			return jsonify(book_list)
		else:
			return 'Nothing Found',404

	if request.method=="POST":
		new_author=request.form['author']
		new_language=request.form['lang']
		new_id=book_list[-1]['id']+1
		new_title=request.form['title']

	new_obj={
	         'id':new_id,
	         'author':new_author,
	         'language':new_language,
	         'title':new_title
	        }

	book_list.appned(new_obj)

	return jsonify(book_list)

if __name__=='__main__':
	app.run(debug=True)