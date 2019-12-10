import flask
import time
import os
import subprocess
import deploy_k8s
import service_with_k8s
app = flask.Flask(__name__)

@app.route('/get/<string:lang>',methods =['GET'])
def fetech_data(lang):
    if lang == "python":
        deploy_k8s.create_my_delploy()
        time.sleep(5)
        service_with_k8s.create_my_service()
        time.sleep(5)
    ur_url = subprocess.getoutput("minikube service ssh-python-service --url")

    return ur_url,"Hello Sultan Mirza This container 2 flask !!!!!!!!!!!!1"

# @app.route('/get/make_ssh',methods =['GET'])
# def make_ssh_con():
#     os.system("mkdir flask_dir")
#     # os.system("sshpass -p gslab@123 ssh gslab@192.168.1.106")
#     os.system("python3 ssh_w_python.py")
#     return "Your python code for ssh is running...... "



if __name__ == "__main__":
    app.run(debug=True,port=5005,host='0.0.0.0')