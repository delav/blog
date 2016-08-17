KindEditor.ready(function(K) {
                K.create('textarea[name=content]',{
                    width:'800px',
                    height:'300px',
                    uploadJson: '/admin/upload/kindeditor'
                });
        });