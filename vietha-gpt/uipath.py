import json
import requests
class runJobs:
    def __init__(self) -> None:
        self.processName = None
        self.user_data = """{ 
    "grant_type": "refresh_token" ,
    "client_id": "8DEv1AMNXczW3y4U15LL3jYf62jK93n5",
    "refresh_token": "F4T4c2__-WzPD6k24LkRmGEA9BeBJUEnuUJ2pyGH1i_mM"
    }"""
        self.orchestrator_url = f"https://cloud.uipath.com/ihccngngh/DefaultTenant/orchestrator_"

        self.folder_id = str(self.getFolderID())
        self.getReleaseKeyID = str(self.getReleaseKeyID)
        self.runJob = self.runJob
    def getUserToken(self, user_data):
        url = f"https://account.uipath.com/oauth/token"
        data = requests.post(url,json=json.loads(user_data))
        authentication_data = json.loads(data.text)
        token = "Bearer " + str(authentication_data['access_token'])
        return token

    def getFolderID(self, orchestrator_url):
        url = orchestrator_url + f"/odata/folders"
        headers = {
        "Authorization": "Bearer " + "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6InZldG5hbmcxMTAyQGdtYWlsLmNvbSIsImh0dHBzOi8vdWlwYXRoL2VtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FjY291bnQudWlwYXRoLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTY1MzYwNTE2MjY4ODk3NjQxNCIsImF1ZCI6WyJodHRwczovL29yY2hlc3RyYXRvci5jbG91ZC51aXBhdGguY29tIiwiaHR0cHM6Ly91aXBhdGguZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY5NTk1NDE4OSwiZXhwIjoxNjk2MDQwNTg5LCJhenAiOiI4REV2MUFNTlhjelczeTRVMTVMTDNqWWY2MmpLOTNuNSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MifQ.of-pKA2vXGA1ZzNGnJjhT9JAPccTfy6m_dTo4kFCR6grrpNuuhJvJ7s2zhCAQdCj4SWCMl69Q9sYfwbzkhmDLOPmftbCU6opQcZEjFfb3jVSPt1b5ZJcJMdAc_tlgSOyiVUOaKjONge9VTtOj5jJ7j2d4OB-VBWUa58j_IKkdAAUiHwbVn5-mlgKC_2fwLqmXkxGYbjiw_Dh7igsgzB4E1FdG7rzJYLL4YWvuviMsr5CDdXmBMo8-mnni_cuPeCH_z78DV0xxgzv4NPa_0RDdh9T88dQTar-MkE-m2udlFiuvz8O1KqQfkG7535wh_yQcN2Oh1JHpV5OKvMNy4AAAw",
        "Content-Type": "application/json"
        }
        folder_data = requests.get(url, headers=headers)
        folder_json = json.loads(folder_data.text)
        desired_display_name = "Shared"
        for item in folder_json["value"]:
            if item.get("DisplayName") == desired_display_name:
                folder_id = item.get("Id")
                break
        return folder_id

    def getReleaseKeyID(self, folder_id, processName, orchestrator_url):

        headers = {
            "Authorization": "Bearer " + "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6InZldG5hbmcxMTAyQGdtYWlsLmNvbSIsImh0dHBzOi8vdWlwYXRoL2VtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FjY291bnQudWlwYXRoLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTY1MzYwNTE2MjY4ODk3NjQxNCIsImF1ZCI6WyJodHRwczovL29yY2hlc3RyYXRvci5jbG91ZC51aXBhdGguY29tIiwiaHR0cHM6Ly91aXBhdGguZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY5NTk1NDE4OSwiZXhwIjoxNjk2MDQwNTg5LCJhenAiOiI4REV2MUFNTlhjelczeTRVMTVMTDNqWWY2MmpLOTNuNSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MifQ.of-pKA2vXGA1ZzNGnJjhT9JAPccTfy6m_dTo4kFCR6grrpNuuhJvJ7s2zhCAQdCj4SWCMl69Q9sYfwbzkhmDLOPmftbCU6opQcZEjFfb3jVSPt1b5ZJcJMdAc_tlgSOyiVUOaKjONge9VTtOj5jJ7j2d4OB-VBWUa58j_IKkdAAUiHwbVn5-mlgKC_2fwLqmXkxGYbjiw_Dh7igsgzB4E1FdG7rzJYLL4YWvuviMsr5CDdXmBMo8-mnni_cuPeCH_z78DV0xxgzv4NPa_0RDdh9T88dQTar-MkE-m2udlFiuvz8O1KqQfkG7535wh_yQcN2Oh1JHpV5OKvMNy4AAAw",
            "X-UIPATH-OrganizationUnitId": folder_id
        }
        robot_name = requests.get(orchestrator_url + f"/odata/Releases",
                              headers=headers)
    
        relaesekey_json_obj = json.loads(robot_name.text)
        desired_display_name = processName
        for item in relaesekey_json_obj["value"]:
            if item.get("DisplayName") == desired_display_name:
                releasekey = item.get("key")
                break
        return releasekey
    

    def runJob(self, orchestrator_url,folder_id, releasekey):
        headers = {
        "Authorization": "Bearer " + "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJUTkVOMEl5T1RWQk1UZEVRVEEzUlRZNE16UkJPVU00UVRRM016TXlSalUzUmpnMk4wSTBPQSJ9.eyJodHRwczovL3VpcGF0aC9lbWFpbCI6InZldG5hbmcxMTAyQGdtYWlsLmNvbSIsImh0dHBzOi8vdWlwYXRoL2VtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2FjY291bnQudWlwYXRoLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTY1MzYwNTE2MjY4ODk3NjQxNCIsImF1ZCI6WyJodHRwczovL29yY2hlc3RyYXRvci5jbG91ZC51aXBhdGguY29tIiwiaHR0cHM6Ly91aXBhdGguZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY5NTk1NDE4OSwiZXhwIjoxNjk2MDQwNTg5LCJhenAiOiI4REV2MUFNTlhjelczeTRVMTVMTDNqWWY2MmpLOTNuNSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MifQ.of-pKA2vXGA1ZzNGnJjhT9JAPccTfy6m_dTo4kFCR6grrpNuuhJvJ7s2zhCAQdCj4SWCMl69Q9sYfwbzkhmDLOPmftbCU6opQcZEjFfb3jVSPt1b5ZJcJMdAc_tlgSOyiVUOaKjONge9VTtOj5jJ7j2d4OB-VBWUa58j_IKkdAAUiHwbVn5-mlgKC_2fwLqmXkxGYbjiw_Dh7igsgzB4E1FdG7rzJYLL4YWvuviMsr5CDdXmBMo8-mnni_cuPeCH_z78DV0xxgzv4NPa_0RDdh9T88dQTar-MkE-m2udlFiuvz8O1KqQfkG7535wh_yQcN2Oh1JHpV5OKvMNy4AAAw",
        "X-UIPATH-OrganizationUnitId": folder_id,
        "Content-Type": "application/json"
        }
       
        start_job_json = """{ "startInfo":
       { "ReleaseKey": \"""" + releasekey + """\",
         "Strategy": "ModernJobsCount",
         "JobsCount": 1,
         "InputArguments": "{}"        
       } 
    }"""  # InputArguments should be left {} or not included if workflow does not accept any input
        start_job_data = requests.post(orchestrator_url + f"/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs",
                                   json=json.loads(start_job_json), headers=headers)
        return start_job_data
