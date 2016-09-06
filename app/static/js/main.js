app = angular.module("chatApp", ['ngMaterial', 'ngRoute']);

app.config(function($routeProvider, $locationProvider) {
    $routeProvider.when('/html/index.html', {
        templateUrl: '../templates/enquiries.tpl.html',
        controller: 'enquiryController'
    })

    .otherwise({
        redirectTo: '/html/index.html'
    });

    $locationProvider.html5Mode(true);
});

app.controller('enquiryController', function() {

})
