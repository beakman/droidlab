'use strict';

angular.module('droidlabApp')

    .factory('API', function API($q, $http, $location){

        var api = '/api/';

        var user = {};

        return {

            getUser: function(){
                return user;
            },

            getUsername: function(){
                return user.username;
            },

            setUser: function(userObj){
                user = userObj;
                console.log("setUser:", userObj);
            },

            fetchUser: function(){
                var deferred = $q.defer();
                $http.get(api+'me')
                  .success(function(data){
                    deferred.resolve(data);
                  })
                  .error(function(data){
                    deferred.reject(data);
                  });
                return deferred.promise;
            },

            myProfile: function(){
                var deferred = $q.defer();
                $http.get(api+'me')
                  .success(function(data){
                    deferred.resolve(data);
                  })
                  .error(function(msg, code){
                    deferred.reject(msg);
                  });
                return deferred.promise;
            },

            readProfile: function(pk){
                var deferred = $q.defer();
                $http.get(api+'users/'+pk)
                  .success(function(data){
                    deferred.resolve(data);
                  })
                  .error(function(msg, code){
                    deferred.reject(msg);
                  });
                return deferred.promise;
            }

        };
    })
;