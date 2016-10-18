'use strict';

angular.module('droidlabApp')

  .controller('UserCtrl',
  function UserCtrl($scope, $rootScope, $location, API) {

    $scope.user = false;

    API.fetchUser()
        .then(function(data){
            console.log("fetchdata", data);
            $scope.user = data[0];
            API.setUser(data[0]);
        })
    ;

    $rootScope.$on('djangoAuth.logged_in', function (){
        API.fetchUser()
            .then(function(data){
                console.log("fetchdata", data);
                $scope.user = data[0];
                API.setUser(data[0]);
            })
        ;
        $location.path('/');
    });

    $rootScope.$on('djangoAuth.logged_out', function (){
      console.log("user ctrl sees logout on rootscope")
      //$scope.user = API.getUsername();
        $scope.user = false;
        $location.path('/');
    });

  })
;