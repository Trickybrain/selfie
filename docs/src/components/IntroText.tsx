import clsx from "clsx";
import { Button } from "./Button";
import Link from "next/link";

export function IntroText() {
  return (
    <div
      className={clsx([
        "w-full",
        "flex",
        "flex-col",
        "absolute",
        "top-[529px]",
        "gap-[30px]",
        "wide-phone:top-[184px]",
        "wide-phone:items-end",
        "wide-phone:text-right",
        "tablet:top-[262px]",
        "tablet:gap-[40px]",
        "desktop:top-[345px]",
      ])}
    >
      <p
        className={clsx([
          "text-[20px]",
          "leading-[1.25em]",
          "tablet:text-[30px]",
          "desktop:text-[45px]",
        ])}
      >
        Which is <br className="tablet:hidden" />{" "}
        <Link
          href="#literal"
          scroll={false}
          className="cursor-pointer underline hover:text-blue"
        >
          literal
        </Link>
        ,{" "}
        <Link
          href="#lensable"
          scroll={false}
          className="cursor-pointer underline hover:text-blue"
        >
          lensable
        </Link>
        <br /> and{" "}
        <Link
          href="#like-a-filesystem"
          scroll={false}
          className="cursor-pointer underline hover:text-blue"
        >
          like a filesystem
        </Link>
      </p>
      <Link href="/jvm/get-started">
        <Button
          className={clsx([
            "w-[154px]",
            "h-[35px]",
            "rounded-[10px]",
            "text-[22px]",
            "tablet:w-[154px]",
            "desktop:w-[232px]",
            "text-black",
            "bg-white",
            "shadow-button",
            "tablet:shadow-button-tablet",
            "hover:text-white",
            "hover:bg-blue",
          ])}
        >
          get started
        </Button>
      </Link>
      <div
        className={clsx([
          "text-[18px]",
          "leading-[1.2em]",
          "grid",
          "gap-[30px]",
          "tablet:text-[22px]",
          "desktop:text-[34px]",
        ])}
      >
        <p>
          Snapshot testing is the <br />{" "}
          <span className="text-blue">fastest and most precise</span>
          <br />
          mechanism to{" "}
          <span className="text-red">
            record <br /> and specify
          </span>{" "}
          the <br />
          <span className="text-green">
            behavior of your <br />
            system and its <br />
            components
          </span>
          .
        </p>
        <p>
          Robots are <br /> writing their <br />
          own code. Are
          <br /> you still writing
          <br />
          assertions by <br />
          hand?
        </p>
      </div>
    </div>
  );
}
