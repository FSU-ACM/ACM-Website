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
        .pipe(gulp.dest(build + '/css'));
});

gulp.task('assets', function() {
    gulp.src('src/public/img/**')
        .pipe(flatten())
        .pipe(gulp.dest(build + '/assets/img'))
});

gulp.task('clean', function() {
    var clean = require('gulp-clean');
    gulp.src('html/**', {read:false})
        .pipe(clean());
});

gulp.task('watch', ['build'], function() {
    gulp.watch('src/views/**/*.pug', ['pug']);
    gulp.watch('src/views/**/*.sass', ['sass']);
    gulp.watch('src/public/**', ['assets']);
    gulp.watch('src/locals.js', ['pug'])
});

gulp.task('views', ['pug', 'sass']);
gulp.task('build', ['views', 'assets']);
gulp.task('default', ['build']);
