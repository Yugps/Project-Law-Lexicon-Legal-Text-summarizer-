from transformers import LEDForConditionalGeneration, LEDTokenizer,pipeline
locally_saved_model=LEDForConditionalGeneration.from_pretrained('summarization_model')
locally_saved_tokenizer=tokenizer=LEDTokenizer.from_pretrained('Legal_model_tokenizer_directory')

from pyngrok import ngrok
from flask import Flask,request,render_template
import nltk

app=Flask(__name__)
port_no = 5000
ngrok.set_auth_token('2dW7qeQXYf1RbmtHWu1mUriKQnC_6qjCtetiLtbfKXVY6R1ZZ')
public_url = ngrok.connect(port_no).public_url

@app.route('/')
def homepage():
  return render_template('index.html')

@app.route('/summary_generation',methods=['POST','GET'])
def main_function():
  output=''
  input_article=''
  if request.method=='POST':
    try:
      pipe1 = pipeline("summarization", model=locally_saved_model,tokenizer=locally_saved_tokenizer,device=0)

      length_parameter=int(request.form.get('length_of_summary_required'))
      input_article=request.form.get('main_article')
      gen_kwargs={'length_penalty':1.0,'max_length':length_parameter,'num_beams':16}
      output_summary=pipe1(input_article,**gen_kwargs)
      output=output_summary[0]['summary_text']

    except Exception as e:
      output=e

  return render_template('results.html',original_text=input_article, summary=output)

print(f'here is your global link {public_url}')

if __name__=='__main__':
  app.run(port=port_no)