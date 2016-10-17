'use strict';

angular.module('droidlabApp')
  .controller('MainCtrl', function ($scope, $cookies, $location, djangoAuth) {
    
    $scope.login = function(){
      djangoAuth.login(prompt('Username'),prompt('password'))
      .then(function(data){
        handleSuccess(data);
      },handleError);
    }
    
    $scope.logout = function(){
      djangoAuth.logout()
      .then(handleSuccess,handleError);
    }
    
    $scope.resetPassword = function(){
      djangoAuth.resetPassword(prompt('Email'))
      .then(handleSuccess,handleError);
    }
    
    $scope.register = function(){
      djangoAuth.register(prompt('Username'),prompt('Password'),prompt('Email'))
      .then(handleSuccess,handleError);
    }
    
    $scope.verify = function(){
      djangoAuth.verify(prompt("Please enter verification code"))
      .then(handleSuccess,handleError);
    }
    
    $scope.goVerify = function(){
      $location.path("/verifyEmail/"+prompt("Please enter verification code"));
    }
    
    $scope.changePassword = function(){
      djangoAuth.changePassword(prompt("Password"), prompt("Repeat Password"))
      .then(handleSuccess,handleError);
    }
    
    $scope.profile = function(){
      djangoAuth.profile()
      .then(handleSuccess,handleError);
    }
    
    $scope.updateProfile = function(){
      djangoAuth.updateProfile({'first_name': prompt("First Name"), 'last_name': prompt("Last Name"), 'email': prompt("Email")})
      .then(handleSuccess,handleError);
    }
    
    $scope.confirmReset = function(){
      djangoAuth.confirmReset(prompt("Code 1"), prompt("Code 2"), prompt("Password"), prompt("Repeat Password"))
      .then(handleSuccess,handleError);
    }

    $scope.goConfirmReset = function(){
      $location.path("/passwordResetConfirm/"+prompt("Code 1")+"/"+prompt("Code 2"))
    }
    
    var handleSuccess = function(data){
      $scope.response = data;
    }
    
    var handleError = function(data){
      $scope.response = data;
    }

    $scope.profile();
    $scope.user = $scope.response;

    $scope.show_login = true;
    $scope.$on("djangoAuth.logged_in", function(data){
      $scope.show_login = false;
    });
    $scope.$on("djangoAuth.logged_out", function(data){
      $scope.show_login = true;
    });

  });

angular.module('droidlabApp')
  .controller('ExperimentsCtrl', function($scope, $http){
    
    $scope.getExperiments = function() {
      $scope.loading = true;
      $scope.experiments = [];
      var url = 'http://127.0.0.1:8000/api/';
      $http.get(url)
          .success(function(data) {
            $scope.experiments = data;
          })
          .error(function(data, status) {
              alert('Error getting experiments!');
          }).finally(function() {
              $scope.loading = false;
          });
    }

    $scope.getExperiments();

  });

angular.module('droidlabApp')
  .controller('ExperimentCtrl', function($scope, $http, $routeParams){
    $scope.experiment_name = $routeParams.experimentName;
    $scope.getResults = function() {
      $scope.loading = true;
      $scope.results = [];
      var url = 'http://127.0.0.1:8000/api/'+ $scope.experiment_name + '/results';
      $http.get(url)
          .success(function(data) {
            $scope.results = data;
          })
          .error(function(data, status) {
              alert('Error getting results!');
          }).finally(function() {
              $scope.loading = false;
          });
    }

    $scope.getResults();

  });  