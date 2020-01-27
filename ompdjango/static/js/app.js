Vue.component('greeting', {
    template: '<h2>{{message}}</h2>',
    props: {
        message: {
            type: String,
            required: true
        }
    },
    methods: {},
    computed:{},
});

new Vue({
  delimiters: ['[[', ']]'],
  el: '#workflow',
  data: {
    title: 'sss'
  }
})