import urllib.request
import xlrd
#adam
workbook = xlrd.open_workbook("2.xlsx")
worksheet = workbook.sheet_by_index(0)
first_row = worksheet._cell_values[0]
list_of_questions = []

for q in first_row:
    list_of_questions.append("aria-label=" + "\"" + q + "\"")

NUM_OF_QUESTIONS = 2
url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfEan9kz5zkPTbyn4Xotg4FDYL5-d9_DAoi_BMGLsQG1JmeKQ/formResponse'
fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

# my_entries_dict = {}
# asci_rep = 66 #B
# cell = chr(asci_rep)
cell = 65
my_entries_dict = {}

my_entries_list = []
for q in list_of_questions:
    # if q in mystr:
    try:
        q=q.strip()
        new_string = mystr.strip().split(q)[1]
    except IndexError:
        print("q: {} \n my_entries_list: {}".format(q, my_entries_list))
        raise

    mystr = mystr.replace(mystr.split(q)[0], "miaoh")
    words = new_string.split(" ")

    entry = None
    wordCounter = 0
    for word in words:
        if wordCounter > 7:
            raise "Haim is stupid. call him. he need to fix the script - 1"
        if "entry" in word:
            entry = word
            entry = entry.split("\"")[1]
            my_entries_list.append(entry)
            wordCounter += 1

            my_entries_dict[chr(cell)] = entry
            cell += 1  # increase to next letter/column

            break
    if not entry:
        raise "Haim is stupid. call him. he need to fix the script -2"

# my_entries_dict[cell] = entry
# cell = chr(ord(cell) + 1) #increase to next letter/column

text_file = open("output.txt", "w+")
text_file.write(str(my_entries_list))
text_file.write("\n")
text_file.write(str(my_entries_dict))  # degub
text_file.write("\n")
text_file.write("\n")
text_file.write("\n")
text_file.write(""" function myFunction() {
  NUMBER_OF_RESPONSES = """)
text_file.write(str(my_entries_list.__len__()))
text_file.write("""\n
  var formURL =""")
text_file.write("'" + url + "'")
text_file.write(""";

  var wrkBk = SpreadsheetApp.getActiveSpreadsheet();
  var wrkSht = wrkBk.getSheetByName("Sheet1");


  my_entries_list =""")
text_file.write(str(my_entries_list))
text_file.write("""
  var rowNum = 2 //first row

  var column_letter;
  var cell;
  var cellValue;
  var datamap = {};
  var addition = ""

  for (i = 0; i < NUMBER_OF_RESPONSES; i++){
    var column_asci = 65 // column - the first is A=65
    for (j = 0; j < my_entries_list.length; j++) 
    {
      if (column_asci>90)
      {
        addition = "A"
        column_asci = 65;
      } 
      column_letter = String.fromCharCode(column_asci);
      cell = addition + column_letter + rowNum.toString();
      cellValue = wrkSht.getRange(cell).getValue();
      if (typeof cellValue != "string"){
        cellValue = parseInt(cellValue);
        cellValue = cellValue.toString()
      }

      datamap[my_entries_list[j]] = cellValue;

      column_asci += 1;
    }
    rowNum +=1;
    j=0;
    addition="";
     var options = {"method" : "post",
                 "payload" : datamap};

    response = UrlFetchApp.fetch(formURL, options);

  }

}""")

text_file.close()

# print ("haim i \"haten\" you")

#
# t = "im am the king of the worls"
#
# a= t.split("king")
# print (a)