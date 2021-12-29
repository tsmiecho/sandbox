import PyPDF2

merger = PyPDF2.PdfFileMerger()
merger.append('./sample/sample.pdf')
merger.append('./sample/dummy.pdf', pages=(0, 1))
merger.write("NewMergedFile.pdf")