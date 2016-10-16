'use strict';

angular.module('droidlabApp')
  .controller('LogoutCtrl', function ($scope, $location, djangoAuth) {
    djangoAuth.logout();
  });
