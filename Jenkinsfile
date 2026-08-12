void setBuildStatus(String message, String state, String repo_url) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: repo_url],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "SUCCESS"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

pipeline {
    agent any

    stages {
        stage('No checks configured') {
            steps {
                echo 'No CI checks are currently configured.'
            }
        }
    }
    post {
     success {
        setBuildStatus("Build succeeded", "SUCCESS", "${GIT_URL}");
     }
     failure {
        setBuildStatus("Build failed", "FAILURE", "${GIT_URL}");
     }
  }
}
