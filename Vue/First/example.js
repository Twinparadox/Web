new Vue({ 
    el: "#app", 
    data: {
      number: 0 // 주사위의 숫자를 저장할 변수
    },
    methods:{
      // 주사위를 던졌을 때 실행되는 함수
      rollDice: function () {
        // 임의의 변수 N을 설정하여 1-6사이의 임의의 숫자를 반환
        let N = Math.floor(Math.random() * (6)) + 1;
        // 인스턴스 내부의 값을 불러올 때는 this를 사용
        this.number = N;
      }
    }
  })