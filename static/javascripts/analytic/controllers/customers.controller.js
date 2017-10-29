(function () {
    'use strict';

    angular
        .module('django-angular.analytic.controllers')
        .controller('CustomersController', CustomersController);


    CustomersController.$inject = ['$scope','$http', '$log','Customers','Snackbar'];

    /**
     * @namespace CustomersController
     */
    function CustomersController($scope, $http, $log,Customers,Snackbar) {

        $http.get('/api/v1/customers/').then(function(response){
               $scope.customers = response.data;
               //$scope.log = $scope.customers;
        });

        /*var lastYearDate = new Date();
        lastYearDate.setFullYear(lastYearDate.getFullYear()-1);
        $scope.date = Math.round(lastYearDate.getTime()/1000);*/
        //moment(new Date()).isAfter(lastYearDate);

        /*$http({
            method: 'GET',
            url: 'https://bo.zelty.fr/app_api/1.0/customers',
            headers: {
                "x-api-key": "28f84ccd190145f5b9e460c565643873dbc8617f"
            }
        }).success(function(data,status,headers,config) {
                $scope.data =data;
                //$scope.log = $scope.data;
        }).error(function(data,status,headers,config){
                alert("failure");
        });*/

       /*Customers.getAll().then(AllCustomersSuccessFn, AllCustomersErrorFn);

       function AllCustomersSuccessFn(response, status, headers, config) {
             $scope.customers = response.data.customers;
             //$scope.log = $scope.customers;
             Snackbar.show('Success! customers data retrieved.');
       }

       function AllCustomersErrorFn(response, status, headers, config) {
              alert("failure");
              Snackbar.error("failure to retrieve data");
       }

        $scope.$watch('log', function() {
             console.log($scope.log );
        });*/

    }

})();