#import src.drukomat_class
import src.program_class


#drukomat_01 = src.drukomat_class.Drukomat()
program_01 = src.program_class.Program()


host = "imap.gmail.com"
username = "dr.grubylolek@gmail.com"
password = 'lkvd djam lizu exmo'
download_folder = "C:/Users/piotr/OneDrive/Pulpit/print-box/pdfs_file"





def main():
    print ("*Program START*")
    # set up section
    program_01.download_pdf_files(host,username,password,download_folder)
    program_01.print_pdf_files()
    
    
    #print ("*Program zaczyna pętle*")
    #while True:



main()
