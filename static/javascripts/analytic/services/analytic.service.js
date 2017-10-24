
(function () {
    'use strict';

    angular
        .module('django-angular.analytic.services')
        .factory('Customers', Customers);

    Customers.$inject = ['$http', 'Authentication'];

    /**
     * @namespace Customers
     * @returns {Factory}
     */
    function Customers($http, Authentication) {
        var Customers = {
            getAll: getAll,
            create: create,
            get: get,
            getHistory: getHistory,
            update: update,
            delete: deleteCustomer,
        };

        return Customers;

        ////////////////////

        /**
         * @name all
         * @desc Get all Customers
         * @returns {Promise}
         * @memberOf django-angular.analytic.services.Customers
         */
        function getAll() {
            return $http.get('https://bo.zelty.fr/app_api/1.0/customers', {
                             headers: {"x-api-key": "28f84ccd190145f5b9e460c565643873dbc8617f"}});


        }

        /**
         * @name create
         * @desc Create a new Customer
         * @param {string} content The content of the new Post
         * @returns {Promise}
         * @memberOf django-angular.analytic.services.Customers
         */
        function create(content) {
            /*return $http.post('https://bo.zelty.fr/app_api/1.0/customers', {
                author: Authentication.getAuthenticatedAccount(),
                content: content
            });*/
        }

        /**
         * @name get
         * @desc Get a Customer by id
         * @param {int} id of Post
         * @returns {Promise}
         * @memberOf django-angular.analytic.services.Customers
         */
        function get(id) {
            return $http.get('https://bo.zelty.fr/app_api/1.0/customer/' + id, {
                             headers: {"x-api-key": "28f84ccd190145f5b9e460c565643873dbc8617f"}});
        }


        /**
         * @name getHistory
         * @desc Get all transaction per Customer by id
         * @param {int} id of Post
         * @returns {Promise}
         * @memberOf django-angular.analytic.services.Customers
         */
        function getHistory(id) {
            return $http.get('https://bo.zelty.fr/app_api/1.0/customer/' + id + '/history', {
                             headers: {"x-api-key": "28f84ccd190145f5b9e460c565643873dbc8617f"}});
        }


        /**
         * @name update
         * @desc Update a Customer by id
         * @param {int} id of Post
         * @param {string} content The content of the Post
         * @returns {Promise}
         * @memberOf django-angular.analytic.services.Customers
         */
        function update(id, content) {
            /*return $http.put('/api/v1/posts/' + id + '/', {
                content: content
            });*/
        }

        /**
         * @name delete
         * @desc Delete a Customer by id
         * @param {int} id of Post
         * @returns {Promise}
         * @memberOf django-angular.analytic.services.Customers
         */
        function deleteCustomer(id) {
            //return $http.delete('/api/v1/posts/' + id + '/');
        }


    }
})();