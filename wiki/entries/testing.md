kjewkfjbwkjefb      markdown=Markdown()

                util.save_entry(title,data)

                save=util.get_entry(title)

                s=markdown.convert(save)

                

                return render(request,"encyclopedia/found.html",{

            "entry":s,

            "Title":title,

        })