Project-202: Docker Swarm Deployment of Phonebook Application (Python Flask) with
- Infrastructure
    - Public Repository on Github (Codebase, Versionig System)
    - Docker Swarm as Orchestrator
        - 3 Manager
        - 2 Worker
    - Image Repository (AWS ECR)
    - Should be able to
        - Every EC2 is able to talk each other (EC2 Connect CLI, IAM Policy)
        - Grand Master can pull image from ECR and push image to AWS ECR
        - Mangers and Workers can pull image from AWS ECR.
- Application Deployement
    - Dockerfile
    - docker-compose.yml (Web server and Mysql)


    docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html

    anahtar-kilit ilişkisi gibi
11:02
asimetrik şifreleme=private+public key
11:03
ssh-keygen


ssh-keygen -t rsa :: kendimiz localde manuel olarak private key oluşturuyoruz...


https://github.com/awslabs/amazon-ecr-credential-helper/blob/master/docs/docker-credential-ecr-login.1


