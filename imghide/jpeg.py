class JPEG:
 
    def write(file_name:str, secret):
        try:
            with open(file_name, 'ab') as f:
                f.write(secret)
            return "Done"
        except Exception as e:
            return e
    
    def read(file_name:str):
        try:
            with open(file_name, 'rb') as f:
                content = f.read()
                offset = content.index(bytes.fromhex('FF09'))
                f.seek(offset + 2)
                final_cont = f.read()
            return str(final_cont)
        except Exception as e:
            return e



