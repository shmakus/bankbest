/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
        config.extraPlugins = 'toc';
        config.toc = {
        title: 'Table of Contents',
        scope: 3,
        listType: 'ul',
        formatSelector: 'h1,h2,h3,h4,h5,h6',
    };

};
