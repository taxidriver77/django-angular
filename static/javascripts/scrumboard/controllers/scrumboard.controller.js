
(function () {
    'use strict';

    angular
        .module('django-angular.scrumboard.controllers')
        .controller('ScrumboardController', ScrumboardController);

    ScrumboardController.$inject = ['$scope','$http','$log'];

    /**
     * @namespace ScrumboardController
     */
    function ScrumboardController($scope, $http,$log) {

              $scope.add = function (list, title) {

                        var card = {
                            list: list.id,
                            title: title
                        };

                        $http.post('/scrumboard/cards/',card)
                            .then(function(response){

                                list.cards.push(response.data);

                                $scope.log = list.cards;
                                console.log(list.cards);

                                $scope.cards = list.cards
                                var url = '/scrumboard/lists/' + list.id + '/';

                                var newList = {
                                    //id: list.id,
                                    name: list.name,
                                    cards: $scope.cards
                                };

                                $http.put(url, newList)
                                    .then(function(response){

                                    },
                                    function(){
                                       alert('Could not update list');
                                    });
                            },
                            function(){
                                alert('Could not create card');
                            });
               };

              $scope.data = [];
              $scope.sortBy = 'story_points';
              $scope.reverse = true;
              $scope.showFilters = false;

              $http.get('/scrumboard/lists/').then(function(response){
                        $scope.data = response.data;
               });

               $scope.$watch('log', function() {
                console.log($scope.log );
              });
    }
})();