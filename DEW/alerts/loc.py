import re

def get_code(zipcode):
    try:
        f = open(r"C:\Users\7390\Documents\django\DEW\alerts\loc.txt", 'r')
        g = open(r"C:\Users\7390\Documents\django\DEW\alerts\zip.txt", 'r')
        locs = f.read()
        zips = g.read()
        zip_out = re.findall("[A-Z,a-z,., ]+"+str(zipcode)+'[A-Z,a-z,., ,,]+', zips)
        #print(zip_out[0])
        county_s = re.findall(r"\w+\.?[ ]?\w*", zip_out[0])
        state = county_s[1]
        #print(county_s[3])
        sort = str(state) + r"\|[A-Z, a-z, 0-9,|]+" + str(county_s[3])
        out = re.findall(sort, locs)
        #print(out[0])
        code_s = re.findall(r"\w+", out[0])
        #print(code_s[1])
        code = "MOZ"+str(code_s[1])
        f.close()
        return code
    except:
        return 0
    

#county = input("Please input your Zipcode: ")
#code = get_code(county)
#print(code)