from win32com import client
from appJar import gui
from pathlib import Path
import temp
import saves
import os

def Excel_to_pdf():
   def excel_to_pdf(input_file,output_file):
      xlApp = client.Dispatch("Excel.Application")
      books = xlApp.Workbooks.Open(input_file)
      ws = books.Worksheets[0]
      ws.Visible = 1
      out_file=str(output_file)# desktop\file.pptx
      out_file+=".pdf"
      ws.ExportAsFixedFormat(0,out_file )
      #print("XLSX to PDF conversion sucessful and Saved")
      if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
           app.stop()


   def validate_inputs(src_file, dest_dir, out_file):

        errors = False
        error_msgs = []
        if Path(src_file).suffix.upper() != ".XLSX":
           errors = True
           error_msgs.append("Please select a .XLSX input file")
           
        if not(Path(dest_dir)).exists():
           errors = True
           error_msgs.append("Please Select a valid output directory")

       # Check for a file name
        if len(out_file) < 1:
           errors = True
           error_msgs.append("Please enter a file name")
           
        return(errors, error_msgs)


   def press(button):
       if button=="Start_Build":
           f=os.getcwd()
           f=f.replace('\\','/')
           src_file = rf'{f}/inprocess/{temp.invoicenum}_{temp.btName}.xlsx' #app.getEntry("Input_File")
           dest_dir = rf'{temp.destPdf}' #app.getEntry("Output_Directory")
           out_file = f"{temp.invoicenum}_{temp.btName}" #app.getEntry("Output_name")
           errors, error_msg = validate_inputs(src_file, dest_dir, out_file)
           if errors:
               app.errorBox("Error", "\n".join(error_msg), parent=None)
           else:
              excel_to_pdf(src_file,Path(dest_dir,out_file))
       else:
           app.stop()


   app=gui("Excel to PDF Converter", useTtk=True)
   app.setTtkTheme('alt')
   app.setSize(150, 10)

   # Add the interactive components
   '''
   app.addLabel("Choose Source Excel File to convert ")
   app.addFileEntry("Input_File")


   app.addLabel("Select Output Directory")
   app.addDirectoryEntry("Output_Directory")

   app.addLabel("Output file name")
   app.addEntry("Output_name")
'''
   app.addButtons(["Start_Build", "Quit"],press)
   app.go()


Excel_to_pdf()
