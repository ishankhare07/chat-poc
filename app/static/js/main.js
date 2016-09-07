app = angular.module("chatApp", ['ngMaterial', 'ngRoute']);

app.config(function($routeProvider, $locationProvider) {
    $routeProvider.when('/html/index.html', {
        templateUrl: '../templates/enquiries.tpl.html',
        controller: 'chatController'
    })

    .otherwise({
        redirectTo: '/html/index.html'
    });

    $locationProvider.html5Mode(true);
});

app.controller('chatController', function($interval, $timeout, $scope) {
    this.start_time = new Date().getTime();
    this.total_time = 0;
    this.clients = [];
    this.messages = [];
    this.message_count = 0;
    var self = this;

    this.create_clients = function() {
        var ws = new WebSocket("ws://localhost:8888/api/ws");

        ws.onmessage = self.on_message;
        ws.onclose = self.on_close;

        self.clients.push(ws);
    };

    this.on_message = function(message) {
        console.log(message.data);
        self.messages.push(message);
        self.message_count++;
        $scope.$apply();
    };

    this.on_close = function() {
        //self.messages.push("closed");
    };

    this.send_messages = function() {
        self.clients.forEach(function(ws, array, index) {
            if(ws.readyState == 1) {
                console.log("sending");
                ws.send("ping " + new Date().getTime());
                self.message_count++;
                $scope.$apply();
            } else {
                console.log(ws.readyState);
            }
        });
    }

    $interval(this.create_clients, 100);
    $interval(function() {
        self.send_messages();
        self.total_time = ((new Date().getTime()) - self.start_time);
        $scope.$apply();
    }, 500);

    /*this.create_clients();
    $timeout(function() {
        self.send_messages()
    }, 5000);*/
})
