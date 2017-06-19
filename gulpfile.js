const gulp    = require('gulp');
const flatten = require('gulp-flatten')

const build = 'html';

gulp.task('pug', function() {
    const pug    = require('gulp-pug');
    const locals = require('./src/locals.js');

    gulp.src(['src/views/*/*.pug', '!src/views/_includes/**'])
        .pipe(pug({locals: locals}))
        .on('error', console.log)
        .pipe(flatten())
        .pipe(gulp.dest(build));
});

gulp.task('sass', function() {
    const sass = require('gulp-sass');
    const paths = ['src/public/'];
    gulp.src('src/views/**/*.sass')
        .pipe(sass({includePaths: paths})
            .on('error', sass.logError))
        .pipe(flatten())
        .pipe(gulp.dest(build + '/css/'));
});

gulp.task('clean', function() {
    var clean = require('gulp-clean');
    gulp.src('html/**', {read:false})
        .pipe(clean());
});

gulp.task('watch', function() {
    gulp.watch('src/**/*.pug', ['pug']);
    gulp.watch('src/**/*.sass', ['sass']);
});

gulp.task('views', ['pug', 'sass']);
gulp.task('build', ['views']);
gulp.task('default', ['build']);
