var app = new Vue({
	el: '#app',
	data: {
		position: 0,
	},
	created() {
		fetch('/status')
			.then(res => {return res.json()})
			.then(status => {
      this.position = status.position
      console.log(status.position)
      })
			.catch(e => {
				console.log(e);
			});
	},
	methods: {
		up: function () {
			console.log('up');
			fetch('/up')
				.then(res => {return res.json()})
				.then(status => this.position = status.position)
				.catch(e => {
					console.log(e);
				});
			this.position = 100;
		},
		down: function () {
			console.log('down');
			fetch('/down')
				.then(res => {return res.json()})
				.then(status => this.position = status.position)
				.catch(e => {
					console.log(e);
				});
		},
		moveTo: function () {
			fetch('/height/'+this.position)
				.then(res => {return res.json()})
				.then(status => this.position = status.position)
				.catch(e => {
					console.log(e);
					this.position = 100;
				});
		},
	},
});
