(function(){
      'use strict';

       angular.module('django-angular.scrumboard.directives')
              .directive('scrumboardCard', CardDirective);

       function CardDirective(){

            return {

                templateUrl: '/static/templates/scrumboard/card.html',
                restrict: 'E',
                //controllerAs: 'cardCtrl',
                controller: ['$scope','$http', function ($scope,$http){

                    var url = '/scrumboard/cards/' + $scope.card.id + '/';
                    $scope.destList = $scope.list;

                    $scope.update = function(){
                        return $http.put(
                               url,
                               $scope.card
                        );
                    };

                    function removeCardFromList(card,list){
                                var cards = list.cards;
                                cards.splice(
                                    cards.indexOf(card),
                                    1
                                );
                    }

                    $scope.delete = function(){
                        $http.delete(url).then(
                            function(){
                                removeCardFromList($scope.card,$scope.list);
                            }
                        );
                    };

                    $scope.move = function(){
                        if ($scope.destList === undefined){
                            return;
                        }
                        $scope.card.list = $scope.destList.id;
                        $scope.update().then(function (){
                            {
                                removeCardFromList($scope.card, $scope.list);
                                $scope.destList.cards.push($scope.card);
                            }
                        });

                    };

                    $scope.modelOptions = {
                        debounce: 500
                    };
                }]
            };
       }
})();