'use strict';

angular.module('droidlabApp')
  .controller('ExperimentsCtrl', function($scope, $http, $window){
    
    $scope.getExperiments = function() {
      $scope.loading = true;
      $scope.experiments = [];
      var url = '//' + $window.location.host + '/api/';
      $http.get(url)
          .success(function(data) {
            $scope.experiments = data;
          })
          .error(function(data, status) {
              console.log('Error getting experiments!');
          }).finally(function() {
              $scope.loading = false;
          });
    }

    $scope.getExperiments();

  });

angular.module('droidlabApp')
  .controller('ExperimentCtrl', function($scope, $http, $window, $routeParams){
    $scope.experiment_name = $routeParams.experimentName;
    $scope.getResults = function() {
      $scope.loading = true;
      $scope.results = [];
      var url = '//' + $window.location.host + '/api/'+ $scope.experiment_name + '/results';
      $http.get(url)
          .success(function(data) {
            $scope.results = data;
          })
          .error(function(data, status) {
              console.log('Error getting results!');
          }).finally(function() {
              $scope.loading = false;
          });
    }

    $scope.getResults();

  }); 