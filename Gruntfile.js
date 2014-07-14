module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),

		minified: {
			files: {
				src: 'application/rally_for_the_cure/static/js/main.js',
				dest: 'application/rally_for_the_cure/static/js/min/'
			},
			options: {
				sourcemap: true,
				allinone: false
			}
		},
		watch: {
			scripts: {
				files: ['application/rally_for_the_cure/static/js/main.js'],
				tasks: ['minified'],
				options: {
					spawn: false
				}
			},
		},
	});

	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-minified');
	grunt.registerTask('default', 'watch');
};