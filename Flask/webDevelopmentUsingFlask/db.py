import json
class Database():
    def add_data(self,name,email,password):
        with open('/Users/aggar/Flask/webDevelopmentUsingFlask/mydb.json','r') as rf:
            data=json.load(rf)
            if email in data:
                return 0
            else:
                data[email]=[name,password]
        with open('/Users/aggar/Flask/webDevelopmentUsingFlask/mydb.json','w') as wf:
                json.dump(data,wf,indent=4)
                return 1   

    def check_data(self,email,password):
         with open('/Users/aggar/Flask/webDevelopmentUsingFlask/mydb.json','r') as rf:
            data=json.load(rf)
            if email in data:
                if password==data[email][1]:
                    return 1
                else:
                    return 0
            else:
                return -1    

