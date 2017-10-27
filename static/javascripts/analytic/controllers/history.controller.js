(function () {
    'use strict';

    angular
        .module('django-angular.analytic.controllers')
        .controller('HistoryController', HistoryController);

    HistoryController.$inject = ['$scope','$http', '$log','$routeParams', 'Customers','Snackbar'];

    /**
     * @namespace HistoryController
     */
    function HistoryController($scope, $http, $log ,$routeParams ,Customers, Snackbar) {

        $scope.customerId = $routeParams.customerId;

        /*Customers.get($scope.customerId).then(CustomerInfoSuccessFn, CustomerInfoErrorFn);
        Customers.getHistory($scope.customerId).then(HistoryCustomersSuccessFn, HistoryCustomersErrorFn);

        function HistoryCustomersSuccessFn(response, status, headers, config) {
             $scope.orders = response.data.orders;
             Snackbar.show('Success! history data retrieved.');
        }

        function HistoryCustomersErrorFn(response, status, headers, config) {
             alert("failure");
             Snackbar.error("failure to retrieve history data");
        }

        function CustomerInfoSuccessFn(response, status, headers, config) {
             $scope.customer = response.data.customer;
             //$scope.log = $scope.customer;
             Snackbar.show('Success! customer data retrieved.');
        }

        function CustomerInfoErrorFn(response, status, headers, config) {
             alert("failure");
             Snackbar.error("failure to retrieve customer data");
        }*/

        $scope.$watch('log', function() {
             console.log($scope.log );
        });
    }
})();