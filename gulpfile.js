require('dotenv').config() // for testing

const gulp = require('gulp')
const gutil = require('gulp-util')
const ftp = require('vinyl-ftp')

gulp.task('deploy', function () {
    const {username, password} = process.env

    var conn = ftp.create({
        host:     'fsu.hosting.acm.org',
        user:     username,
        password: password,
        parallel: 1,
        log:      gutil.log
    })

    // using base = '.' will transfer everything to /public_html correctly
    // turn off buffering in gulp.src for best performance

    return gulp.src('dist/**', { base: 'dist', buffer: false })
        .pipe(conn.dest('public_html/.'))

})
