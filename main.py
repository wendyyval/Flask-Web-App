from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # line only executes if file is run directly...everytime a change happens it will automatically update
    # make false in production

