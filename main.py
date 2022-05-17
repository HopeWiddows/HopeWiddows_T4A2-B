#importing dependencies/libraries
from Notes_App import create_app

#main file, used to run application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)