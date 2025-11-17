from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# create the categories list
categories = [{"id": 1, "name": "Textbooks"},
              {"id": 2, "name": "Study Guides"},
              {"id": 3, "name": "Lab Supplies"},
              {"id", 4, "name": "Other Books"}]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]
books = [[1, 1, "General Chemistry - Atoms to Reactions", "Kevin Revell", "13-9781319589554", "54.99", "static/images/books/textbooks/genchem.png", 1],
         [2, 1, "Organic Chemistry", "Sardine Designs Science", "13-9781794195028", "60.37", "static/images/books/textbooks/orgo.png", 0],
         [3, 1, "Biochemistry 3rd Edition", "Mathews, Van Holde & Ahern", "13-9780805330663", "45.99", "static/images/books/textbooks/biochem.png", 1],
         [4, 1, "The Journal of Physical Chemistry", "American Chemical Society", "13-9781234567897", "30.48", "static/images/books/textbooks/pchem.png", 0],
         [5, 2, "ACS® General Chemistry Study Guide", "Mometrix", "13-9781516722372", "29.99", "static/images/books/study_guide/genchem_guide.png", 1],
         [6, 2, "ACS Organic Chemistry Study Guide", "Joshua Rueda", "13-9781637752029", "58.99", "static/images/books/study_guide/orgo_guide.png", 0],
         [7, 2, "ACE Biochemistry!", "Dr. Holden Hemsworth", "13-9781515013099", "22.99", "static/images/books/study_guide/biochem_guide.png", 1],
         [8, 2, "Preparing for Your ACS Examination in Physical Chemistry", "ACS Exams Institute", "13-9780970804228", "45.99", "static/images/books/study_guide/pchem_guide.png", 0],
         [9, 3, "General Chemistry Laboratory Manual", "Northern Arizona University", "13-9781234567804", "28.99", "static/images/books/lab_sipplies/lab_manual.jpg", 1],
         [10, 3, "Double-Copy Lab Notebook", "New York University", "13-978-1-947321-09-0", "28.99", "static/images/books/lab_sipplies/lab_note.jpg", 0],
         [11, 3, "Laboratory Manual of Biochemistry: Methods and Techniques", "R. S. Sengar, Reshu Chaudhary", "13-9789383305025", "90.00", "static/images/books/lab_sipplies/biochem_manual.jpg", 1],
         [12, 3, "Laboratory Manual of Organic Chemistry (5th ed.)", "Raj K. Bansal", "13-9788122424744", "13.90", "static/images/books/lab_sipplies/orgo_manual.jpg", 0],
         [13, 4, "Careers with STEM Job Kit: Polymer Chemist", "Monash University", "13-9780412036514", "8.88", "static/images/books/others/career.jpg", 1],
         [14, 4, "The History of Chemistry", "John Hudson", "13-9781468464436", "100.30", "static/images/books/others/history.jpg", 0],
         [15, 4, "Focus On Elementary Chemistry, Student Textbook, 3rd Edition", "Rebecca W. Keller", "13-9781941181362", "49.95", "static/images/books/others/kids_chem.jpg", 1], 
         [16, 4, "Lessons in Chemistry: A Novel", "Bonnie Garmus", "13-9780593314487", "19.00", "static/images/books/others/lesson.jpg"]]

# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template()

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable

    # Create a new list called selected_books containing a list of books that have the selected category

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template()

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
