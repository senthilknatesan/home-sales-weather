#############################################################################
#  File Name:  sap1.py
#  Creats the median listings and sold data files to be loaded into the mysql
#############################################################################

input_sold_file = '/Users/senthilnatesan/Desktop/job-search/sap/Zip_MedianSoldPrice_AllHomes.csv'
output_sold_file = '/Users/senthilnatesan/Desktop/job-search/sap/zip_median_sold_2015.csv'
input_list_file = '/Users/senthilnatesan/Desktop/job-search/sap/Zip_MedianListingPrice_AllHomes.csv'
output_list_file = '/Users/senthilnatesan/Desktop/job-search/sap/zip_median_list_2015.csv'


def create_zip_median_sold_file(inf, outf, nz_cnt):
    line_no = 0
    header_word_count = 0
    out_file = open (outf, 'w' )
    invalid_zip = 0
    invalid_zip_data = 0
    good_data = 0
    with open(inf) as f:
        for line in f:
            line = line.strip()
            line_no += 1
            words = line.split(',')
            if (line_no == 1):
                header_word_count = len(words)
                header = words
                continue
            if (len (words) !=  header_word_count ):
                print "Unknown word count. skip the line. " ,line
                continue
            d = dict (zip(header, words))
            s = get_2015_median_sold_or_list_price(d, nz_cnt)
            if s == "":
                invalid_zip_data += 1
                continue
            else:
                good_data += 1
                out_file.write(s)
    out_file.close()

    print ("total lines ", line_no - 1, "good data ", good_data,  "bad data ", invalid_zip_data)

def get_2015_median_sold_or_list_price(d, nz_cnt):

    non_zero_cnt = 0
    z = d.get('"RegionName"')
    if z == None:
        return ""

    state_code = d.get('"State"')
    if ( state_code == '"HI"') or (state_code == '"AK"' ):
        return ""

    z = z[1:6]
    year = "2015"
    s = ""

    for i in range (1, 13):
        month = "%02d" % (i)
        yy_mm = '\"{0}-{1}\"'.format(year, month)
        v = d.get(yy_mm, 0)
        try:
            f = float(v)
        except ValueError:
            f = 0.0

        if (f != 0.0):
            non_zero_cnt += 1

        s = s + '{0},{1},{2}\n'.format(z, yy_mm[1:len(yy_mm)-1], f)

    if ( non_zero_cnt < nz_cnt ):
        return ""

    return s

def main ():
    create_zip_median_sold_file(input_sold_file, output_sold_file, 10)
    create_zip_median_sold_file(input_list_file, output_list_file, 0)

if __name__ == '__main__':
    main()







