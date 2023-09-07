node {
    // Define the location of the SonarQube scanner executable
    def scannerHome = tool name: 'sonarqube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'

    stage('Checkout') {
        // Checkout your source code repository here (e.g., using Git)
        checkout scm
    }

    stage('Static Code Analysis') {
        try {
            // Run your build commands here if needed
            // For example, with Maven:
            bat 'mvn clean install'

            // Run SonarQube scanner for static code analysis in the background
            def scannerArgs = "-Dsonar.projectKey=sonartest -Dsonar.projectName=sonarqubetest -Dsonar.sources=src"
            def sonarScannerCmd = "${scannerHome}\\bin\\sonar-scanner.bat ${scannerArgs}"
            def scannerProcess = bat(script: "start /B ${sonarScannerCmd}", returnStatus: true)

            if (scannerProcess != 0) {
                error("SonarQube analysis failed with exit code: ${scannerProcess}")
            }
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            throw e
        }
    }

    stage('Quality Gate') {
        // Check the SonarQube quality gate status
        def qualityGateStatus = waitForQualityGate()
        if (qualityGateStatus != 'OK') {
            error("SonarQube Quality Gate check failed: ${qualityGateStatus}")
        }
    }
}
// node{

//     stage('Cloning the project'){
// 	    git branch: 'main', url: 'https://github.com/BINDU1822/sonar-jenkins.git'
//         // git 'https://github.com/BINDU1822/ci-cd-jenkins.git'
//     }
//     stage('Sonarqube Static code analysis'){
//         def scannerHome = tool 'sonarqube';
//         withSonarQubeEnv('sonarqube'){
//             sh "${scannerHome}/bin/sonar-scanner \
//             -D sonar.login=admin \
//             -D sonar.password=binduramesh@1822 \
//             -D sonar.projectkey=sonartest \
// 	    -D sonar.exclusions=vendors/**,resources/**,**/*,java \
//             -D sonar.host.url=http://117.208.152.165:9000/"
//         }
//     }
// }

// pipeline {
//     agent any
    
//     stages {
//         stage('Checkout') {
//             steps {
//                 // Checkout your source code repository here
//                 // For example, with Git:
//                 checkout scm
//             }
//         }
        
//         stage('Build') {
//             steps {
//                 // Compile and build your project here
//                 // For example, with Maven:
//                 sh 'mvn clean install'
//             }
//         }
        
//         stage('SonarQube Analysis') {
//             steps {
//                 script {
//                     // Define SonarQube scanner properties
//                     def scannerHome = tool name: 'sonarqube', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
                    
//                     withSonarQubeEnv('sonarqube') {
//                         sh "${scannerHome}/bin/sonar-scanner"
//                     }
//                 }
//             }
//         }
//     }
// }
