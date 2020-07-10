new Vue({
el: '#app',
data: {
    title: 'Hello world',
    link: 'http://google.com',
    finishedLink: '<a href="http://google.com">Google</a>'
},
methods: {
    sayHello(){
    this.title = 'Hello!'; // vue instance 내부의 this는 자신을 가리킨다.
    return this.title;
    }
}
})