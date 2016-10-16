'use strict';

/**
 * @ngdoc function
 * @name droidlabApp.controller:RestrictedCtrl
 * @description
 * # RestrictedCtrl
 * Controller of the droidlabApp
 */
angular.module('droidlabApp')
  .controller('RestrictedCtrl', function ($scope, $location) {
    $scope.$on('djangoAuth.logged_in', function() {
      $location.path('/');
    });
  });
