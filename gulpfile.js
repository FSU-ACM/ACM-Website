const gulp    = require('gulp')
const flatten = require('gulp-flatten')

const build = 'build'

gulp.task('pug', function() {
    const pug    = require('gulp-pug')
    const locals = require('./src/locals.js')

    gulp.src(['src/views/*/*.pug', '!src/views/_includes/**'])
        .pipe(pug({locals: locals}))
        .on('error', console.log)
        .pipe(flatten())
        .pipe(gulp.dest(build))
})

gulp.task('sass', function() {
    const sass = require('gulp-sass')
    const paths = ['src/styles/']
    gulp.src('src/views/**/*.sass')
        .pipe(sass({includePaths: paths})
            .on('error', sass.logError))
        .pipe(flatten())
        .pipe(gulp.dest(build + '/public/css'))
})

gulp.task('js', function () {
    gulp.src('src/js/*.js')
        .pipe(gulp.dest(build + '/public/js'))
})

// gulp.task('babel', function() {
//     const browserify  = require('browserify')
//     const babelify    = require('babelify')
//     const source      = require('vinyl-source-stream')
//     const buffer      = require('vinyl-buffer')
//     const uglify      = require('gulp-uglify')
//     const sourcemaps  = require('gulp-sourcemaps')

//     return browserify({entries: 'src/js/events.js', debug: true})
//         .transform('babelify', { presets: ['env'] })
//         .bundle()
//         .pipe(source('events.js'))
//         .pipe(buffer())
//         .pipe(sourcemaps.init())
//         // .pipe(uglify())
//         .pipe(sourcemaps.write('./maps'))
//         .pipe(gulp.dest(build + '/public/js'))
// })

gulp.task('favicon', function() {
    gulp.src('assets/favicon.png')
        .pipe(gulp.dest(build))
})

gulp.task('assets', ['favicon'], function() {
    gulp.src('assets/img/**')
        .pipe(flatten())
        .pipe(gulp.dest(build + '/public/img'))
})

gulp.task('clean', function() {
    var clean = require('gulp-clean')
    gulp.src(build + '/**', {read:false})
        .pipe(clean())
})

gulp.task('watch', ['build'], function() {
    gulp.watch('src/views/**/*.pug', ['pug'])
    gulp.watch('src/**/events.json', ['pug'])
    gulp.watch('src/**/sponsors.json', ['pug'])
    gulp.watch('src/**/partners.json', ['pug'])
    gulp.watch('src/views/**/*.sass', ['sass'])
    gulp.watch('src/styles/*.sass', ['sass'])
    gulp.watch('public/**', ['assets'])
    gulp.watch('src/locals.js', ['pug'])
})

gulp.task('views', ['pug', 'sass'])
gulp.task('build', ['views', 'assets', 'js'])
gulp.task('default', ['build'])
