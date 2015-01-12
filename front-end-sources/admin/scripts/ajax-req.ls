/**
 * AJAX request abstration
 *
 * @author Viacheslav Lotsmanov
 * @author Andrew Fatkulin
 */

require! {
	\jquery : $
	'./fatal-error-view' : FatalErrorView
}

module.exports = (app, options)!->
	options = {
		data-type: \json
		method: \POST
		error: (xhr, status, err)!->
			app .get-region \container .show new FatalErrorView exception: err
			throw err
	} <<<< options

	$ .ajax options