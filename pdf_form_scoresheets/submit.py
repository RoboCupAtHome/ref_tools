#! /usr/bin/env python

from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return app.send_static_file('form.pdf')

@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    # import ipdb; ipdb.set_trace()
    # When clicking submit on a PDF form (in the Chrome browser at least), the Form Data Format-formatted form is sent as request.data
    scores = parse_fdf(request.data)
    print scores
    # import ipdb; ipdb.set_trace()
    return str(sum([float(score) for score in scores.values()]))

def parse_fdf(fdf):
    '''Example FDF: 
    '%FDF-1.2\r\n1 0 obj\r\n<</FDF<</F<</F(file:///home/loy/Dropbox/RoboCupTC/RuleBook/scoresheets/form2.pdf)/Type/Filespec/UF(file:///home/loy/Dropbox/RoboCupTC/RuleBook/scoresheets/form2.pdf)>>/Fields[<</T(First Name)/V(Loy)>><</T(Last Name)/V(Dummy)>><</T(Email)/V(Spam)>>]>>>>\r\nendobj\r\n\r\ntrailer\r\n<</Root 1 0 R>>\r\n%%EOF\r\n'
    
    Or, when print-ed: 

    %FDF-1.2
    1 0 obj
    <</FDF<</F<</F(file:///home/loy/Dropbox/RoboCupTC/RuleBook/scoresheets/form2.pdf)/Type/Filespec/UF(file:///home/loy/Dropbox/RoboCupTC/RuleBook/scoresheets/form2.pdf)>>/Fields[<</T(First Name)/V(Loy)>><</T(Last Name)/V(Dummy)>><</T(Email)/V(Spam)>>]>>>>
    endobj

    trailer
    <</Root 1 0 R>>
    %%EOF


    <</FDF
        <</F
            <<
                /F(file:///home/loy/Dropbox/RoboCupTC/RuleBook/scoresheets/form2.pdf) 
                /Type/Filespec/UF(file:///home/loy/Dropbox/RoboCupTC/RuleBook/scoresheets/form2.pdf)
            >>
            /Fields[
                <</T(First Name)/V(Loy)>>
                <</T(Last Name)/V(Dummy)>>
                <</T(Email)/V(Spam)>>
            ]
        >>
    >>

    '''
    _, _, after = fdf.partition("/Fields[")
    fieldsstr, _, _ = after.partition("]>>>>")
    #fieldsstr now only contains '<</T(First Name)/V(Loy)>><</T(Last Name)/V(Dummy)>><</T(Email)/V(Spam)>>'

    keys_values = {}

    splits = fieldsstr.split(">><<")
    for split in splits:
        key, _, value = split.strip("<</T(").strip(")>>").partition(")/V(")
        keys_values[key] = value

    return keys_values

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="127.0.0.1",
        port=int("5000"),
        debug=True
  )